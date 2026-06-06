"""
AI Design Patterns Tools - AI设计模式工具
支持设计模式识别、应用、代码生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDesignPatternsTools:
    """
    AI设计模式工具
    支持：识别、应用、生成
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def identify_pattern(self, problem: str) -> Dict:
        """识别适用的设计模式"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下问题识别适用的设计模式：

{problem}

请返回JSON格式：
{{
    "patterns": [
        {{"name": "模式名", "category": "类别", "description": "描述", "applicability": "适用场景"}}
    ],
    "recommended": "推荐模式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"patterns": content}

    def apply_pattern(self, pattern: str, code: str, language: str) -> str:
        """应用设计模式"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将{pattern}模式应用到以下{language}代码：

```{language}
{code[:2000]}
```

要求：
1. 保持功能不变
2. 清晰的模式结构
3. 注释说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_pattern_code(self, pattern: str, language: str, use_case: str) -> str:
        """生成设计模式代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请用{language}实现{pattern}模式：

用例：{use_case}

要求：
1. 完整实现
2. 类型提示
3. 文档字符串
4. 使用示例"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_architecture(self, code: str, language: str) -> Dict:
        """分析架构"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下{language}代码的架构：

```{language}
{code[:2000]}
```

请返回JSON格式：
{{
    "patterns_used": ["使用的模式"],
    "anti_patterns": ["反模式"],
    "coupling": "耦合度",
    "cohesion": "内聚度",
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def suggest_refactoring(self, code: str, language: str) -> List[Dict]:
        """建议重构"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为以下{language}代码提供重构建议：

```{language}
{code[:2000]}
```

请返回JSON格式：
[
    {{"pattern": "模式", "description": "描述", "before": "重构前", "after": "重构后", "benefit": "收益"}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"suggestions": content}]

    def compare_patterns(self, patterns: List[str], scenario: str) -> Dict:
        """比较设计模式"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        patterns_text = ", ".join(patterns)

        prompt = f"""请比较以下设计模式在{scenario}场景中的适用性：

模式：{patterns_text}

请返回JSON格式：
{{
    "patterns": [
        {{"name": "模式", "pros": ["优点"], "cons": ["缺点"], "fit": "适用度"}}
    ],
    "recommendation": "推荐模式"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"comparison": content}


def create_tools(**kwargs) -> AIDesignPatternsTools:
    """创建设计模式工具"""
    return AIDesignPatternsTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Design Patterns Tools")
    print()

    # 测试
    patterns = tools.identify_pattern("需要创建一个全局唯一的配置管理器")
    print(json.dumps(patterns, ensure_ascii=False, indent=2))
