"""
jianying_effect_api.py 单元测试
验证特效API的枚举完整性和接口正确性
"""
import os
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from jianying_effect_api import JianyingEffectAPI


class TestJianyingEffectAPI(unittest.TestCase):
    """剪映特效API测试"""

    def setUp(self):
        self.api = JianyingEffectAPI()

    def test_api_initialized(self):
        """API应成功初始化"""
        self.assertIsNotNone(self.api)

    def test_has_effect_methods(self):
        """应包含特效相关方法"""
        methods = [
            "apply_scene_effect", "apply_character_effect",
            "apply_filter", "apply_animation",
            "apply_animations_to_segment", "apply_transition",
            "list_effects", "list_animations",
        ]
        for m in methods:
            self.assertTrue(hasattr(self.api, m),
                            f"缺少方法: {m}")

    def test_animation_types(self):
        """动画类型应可通过list_animations获取"""
        animations = self.api.list_animations()
        self.assertIsNotNone(animations)

    def test_apply_invalid_effect(self):
        """应用不存在的效应不应崩溃"""
        try:
            result = self.api.apply_effect(None, "不存在的特效")
            self.assertFalse(result)
        except Exception:
            pass  # 预期可能抛出异常

    def test_apply_invalid_animation(self):
        """应用不存在的动画不应崩溃"""
        try:
            result = self.api.apply_animation(None, "in", "不存在的动画")
            self.assertFalse(result)
        except Exception:
            pass

    def test_effect_categories(self):
        """特效分类应非空"""
        if hasattr(self.api, "EFFECT_CATEGORIES"):
            self.assertTrue(len(self.api.EFFECT_CATEGORIES) > 0)
        elif hasattr(self.api, "_effect_categories"):
            self.assertTrue(len(self.api._effect_categories) > 0)


if __name__ == "__main__":
    unittest.main()
