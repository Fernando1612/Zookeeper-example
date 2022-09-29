import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode_ephemero(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)
    
    def test_crear_znode_regular(self):
        tree = Ztree()
        tree.create('/node1', 'algo', False, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')
    
    def test_crear_znode_ephemero_inactivo(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, False, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_borrar_znode_regular(self):
        tree = Ztree()
        tree.create('/node1','algo',False,True,10,'/')
        tree.delete('/node1',0)
        self.assertFalse(tree.exist('/node1'))

    def test_borrar_znode_ephemero(self):
        tree = Ztree()
        tree.create('/node1','algo',True,True,10,'/')
        tree.delete('/node1',0)
        self.assertFalse(tree.exist('/node1'))

    def test_borrar_znode_ephemero_inactivo(self):
        tree = Ztree()
        tree.create('/node1','algo',True,False,10,'/')
        tree.delete('/node1',0)
        self.assertFalse(tree.exist('/node1'))

    def test_cambiar_datos(self):
        tree = Ztree()
        tree.create('/n','algo',True,True,10,'/')
        tree.setData('/n','algo1')
        self.assertEqual(tree.getData('/n'),'algo1')

        
if __name__ == '__main__':
    unittest.main()

