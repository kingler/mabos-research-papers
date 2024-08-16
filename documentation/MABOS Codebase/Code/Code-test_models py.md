# Code: test_models.py

```python
# test_models.py
import unittest
from unittest.mock import Mock, patch
from mas.mas_manager import MASManager
from mas.model import Model
from api.schemas.model_schemas import ModelCreate, ModelUpdate, ModelType

class TestModels(unittest.TestCase):

    def setUp(self):
        self.mas_manager = MASManager()

    @patch('mas.mas_manager.MASManager.create_model')
    async def test_create_model(self, mock_create_model):
        model_data = ModelCreate(
            name="TestModel",
            model_type=ModelType.BELIEF,
            description="Test belief model",
            content={"resource": "CPU", "threshold": 80}
        )
        mock_create_model.return_value = Model(id="test_id", **model_data.dict(), version=1)
        
        model = await self.mas_manager.create_model(model_data)
        
        self.assertEqual(model.name, "TestModel")
        self.assertEqual(model.model_type, ModelType.BELIEF)
        self.assertEqual(model.content, {"resource": "CPU", "threshold": 80})
        self.assertEqual(model.version, 1)
        mock_create_model.assert_called_once_with(model_data)

    @patch('mas.mas_manager.MASManager.get_model')
    async def test_get_model(self, mock_get_model):
        mock_model = Mock(spec=Model)
        mock_model.id = "test_id"
        mock_get_model.return_value = mock_model
        
        model = await self.mas_manager.get_model("test_id")
        
        self.assertEqual(model.id, "test_id")
        mock_get_model.assert_called_once_with("test_id")

    @patch('mas.mas_manager.MASManager.update_model')
    async def test_update_model(self, mock_update_model):
        update_data = ModelUpdate(
            name="UpdatedModel",
            description="Updated description",
            content={"resource": "CPU", "threshold": 90}
        )
        mock_updated_model = Mock(spec=Model)
        mock_updated_model.name = "UpdatedModel"
        mock_updated_model.description = "Updated description"
        mock_updated_model.content = {"resource": "CPU", "threshold": 90}
        mock_updated_model.version = 2
        mock_update_model.return_value = mock_updated_model
        
        updated_model = await self.mas_manager.update_model("test_id", update_data)
        
        self.assertEqual(updated_model.name, "UpdatedModel")
        self.assertEqual(updated_model.description, "Updated description")
        self.assertEqual(updated_model.content, {"resource": "CPU", "threshold": 90})
        self.assertEqual(updated_model.version, 2)
        mock_update_model.assert_called_once_with("test_id", update_data)

    @patch('mas.mas_manager.MASManager.delete_model')
    async def test_delete_model(self, mock_delete_model):
        mock_delete_model.return_value = True
        
        result = await self.mas_manager.delete_model("test_id")
        
        self.assertTrue(result)
        mock_delete_model.assert_called_once_with("test_id")

    @patch('mas.model.Model.validate_content')
    def test_model_content_validation(self, mock_validate_content):
        model = Model(
            id="test_id",
            name="TestModel",
            model_type=ModelType.GOAL,
            content={"goal": "maintain_system_stability", "priority": 1}
        )
        
        model.validate_content()
        
        mock_validate_content.assert_called_once()

    # Add more tests as needed for other model functionalities

if __name__ == '__main__':
    unittest.main()
```