from dict import HashTable

class TestHashTable(object):
    def test_hash_put(self):
        ht = HashTable()
        ht.put('cat', "meow")
        assert ht.slots[ht.hash('cat')].data == "meow"
        ht.put('cat', "meow meow")
        assert ht.slots[ht.hash('cat')].data == "meow meow"
        assert ht.slots[ht.hash('cat')].next == None
        ht.put('derp', "herp")
        assert ht.slots[3].data == "meow meow"
        assert ht.slots[3].key == "cat"
        assert ht.slots[3].next.data == "herp"
        assert ht.slots[3].next.key == "derp"

    def test_hash_get(self):
        ht = HashTable()
        ht.put('cat', "meow")
        assert ht.get('cat') == 'meow'
        assert ht.get('cat', "foobar") == 'meow'
        assert ht.get('derp', "foobar") == 'foobar'
        assert ht.get('derp') == None
        ht.put('derp', "hello world")
        assert ht.get('derp') == "hello world"
        assert ht.get('derp', "foobar") == 'hello world'

    def test_hash_getters_setters(self):
        ht = HashTable()
        ht['cat'] = "meow"
        assert ht['cat'] == "meow"
        ht['cat'] = "scratch scratch"
        assert ht['cat'] == "scratch scratch"
        assert ht['foo'] == None

    def test_hash_iterator(self):
        ht = HashTable()
        ht['cat'] = "meow"
        ht['foo'] = "bar"
        ht['casey'] = "small"
        ht['small'] = "casey"
        assert "small" in ht.keys
        assert "herp" not in ht.keys
        assert "meow" in ht.values
        assert "cat" not in ht.values
