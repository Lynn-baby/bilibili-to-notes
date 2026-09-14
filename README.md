# bilibili-to-notes

将 B 站视频字幕整理成结构化中文 Markdown 笔记的 Codex Skill。

它可以获取 B 站视频的中文字幕，去除口语化表达、机械重复和推广内容，提炼核心观点，并按照主题组织成便于阅读和回看的 Markdown 笔记。

## 功能

- 支持 `bilibili.com` 和 `b23.tv` 视频链接
- 支持已有 SRT 字幕文件
- 优先获取中文字幕和平台自动字幕
- 去除语气词、口头禅和机械重复
- 删除课程价格、报名引流和社群宣传
- 按主题而不是单纯按时间顺序组织内容
- 保留关键案例、因果关系、限制条件和时间定位
- 输出结构化中文 Markdown 笔记
- 提供 SRT 字幕转带时间戳文本的 Python 脚本

## 项目结构

```text
bilibili-to-notes/
├── LICENSE
├── README.md
├── SKILL.md
├── .gitignore
├── agents/
│   └── openai.yaml
└── scripts/
    └── srt_to_text.py# bilibili-to-notes

将 B 站视频字幕整理成结构化中文 Markdown 笔记的 Codex Skill。

它可以获取 B 站视频的中文字幕，去除口语化表达、机械重复和推广内容，提炼核心观点，并按照主题组织成便于阅读和回看的 Markdown 笔记。

完整行为规则请参阅 [SKILL.md](SKILL.md)。
