# test_profilermemory.py
"""
Tests for ProfilerMemory module.
"""

import unittest
from profilermemory import ProfilerMemory

class TestProfilerMemory(unittest.TestCase):
    """Test cases for ProfilerMemory class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProfilerMemory()
        self.assertIsInstance(instance, ProfilerMemory)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProfilerMemory()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
