# 🎨 AI Design Patterns Tools

AI设计模式工具，支持设计模式识别、应用、代码生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔍 设计模式识别
- 🎨 设计模式应用
- 💻 模式代码生成
- 📊 架构分析
- ♻️ 重构建议
- ⚖️ 模式比较

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_design_patterns_tools import create_tools

tools = create_tools()

# 识别模式
patterns = tools.identify_pattern("需要全局唯一的配置管理器")

# 应用模式
refactored = tools.apply_pattern("单例模式", code, "Python")

# 生成代码
code = tools.generate_pattern_code("观察者模式", "Python", "事件系统")

# 分析架构
analysis = tools.analyze_architecture(code, "Python")

# 重构建议
suggestions = tools.suggest_refactoring(code, "Python")

# 比较模式
comparison = tools.compare_patterns(["单例", "工厂", "建造者"], "配置管理")
```

## 📁 项目结构

```
ai-design-patterns-tools/
├── tools.py       # 设计模式工具核心
└── README.md
```

## 📄 许可证

MIT License
