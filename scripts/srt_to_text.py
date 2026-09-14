#!/usr/bin/env python3
"""Convert SRT to timestamped text without silently dropping malformed cues."""
import argparse
import re
from pathlib import Path

TIMING = re.compile(r'^(\d{2,}:\d{2}:\d{2})[,.]\d{3}\s+-->\s+(\d{2,}:\d{2}:\d{2})[,.]\d{3}(?:\s+.*)?$')


def convert(source):
    result = []
    end = None
    for index, block in enumerate(re.split(r'\n\s*\n', source.strip()), 1):
        lines = block.strip().splitlines()
        if lines and lines[0].strip().isdigit():
            lines = lines[1:]
        match = TIMING.fullmatch(lines[0].strip()) if lines else None
        if not match or len(lines) < 2:
            raise ValueError(f'Invalid or empty SRT cue {index}')
        body = ' '.join(line.strip() for line in lines[1:]).strip()
        if not body:
            raise ValueError(f'Empty text in SRT cue {index}')
        result.append(f'[{match[1]}] {body}')
        end = match[2]
    return '\n'.join(result) + '\n', len(result), end


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error('Output must not overwrite source subtitles')
    try:
        output, count, end = convert(args.source.read_text(encoding='utf-8-sig'))
    except ValueError as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        stream.write(output)
    print(f'{count} cues; final cue ends at {end}; saved to {args.output.resolve()}')


if __name__ == '__main__':
    main()
