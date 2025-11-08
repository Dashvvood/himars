# tests/smoke_test.py
def test_basic_import():
    """验证包能否被正常导入"""
    import himars  # 替换为你的包名
    assert himars.__version__ == "0.1.0"  # 验证版本号是否正确（与 pyproject.toml 一致）

def test_core_function():
    """验证一个核心函数能否正常工作"""
    from himars import hello  # 导入核心函数
    hello()
    
if __name__ == "__main__":
    test_basic_import()
    test_core_function()
    print("Smoke test passed!")