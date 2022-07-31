from os import stat
import sys
sys.path.append('src')
import trie, utils, rlp

#initialize trie from previous hash; add new entry with same key.
state = trie.Trie('wxt-trie', trie.BLANK_ROOT)
state.update('\x01\x01\x02', rlp.encode(['hello']))
print state.root_hash.encode('hex')
print state.root_node
print '----------------------'

"""
state.update('\x01\x01\x02', rlp.encode(['hellothere']))
print state.root_hash.encode('hex')
print state.root_node
#state.update('\x01\x01\x02', rlp.encode(['hellothere']))
#print state.root_hash.encode('hex')
print '-----------------------'"""
"""

state.update('\x01\x01\x03', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
k, v = state.root_node
print 'root node:', [k, v] 

print state._get_node_type(state.root_node) == trie.NODE_TYPE_EXTENSION
common_prefix_key, node_hash = state.root_node 
print state._decode_to_node(node_hash)
print state._get_node_type(state._decode_to_node(node_hash)) == trie.NODE_TYPE_BRANCH
print '***********************************'
"""
"""
state.update('\x01\x01', rlp.encode(['end at branch']))
print 'root hash:', state.root_hash.encode('hex')
print state.root_node
print state._decode_to_node(state.root_node[1]) """

state.update('\x01\x01\x02\x55', rlp.encode(['kaixng2']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
print 'branch node it points to:', state._decode_to_node(state.root_node[1])
print '***********************************'

state.update('\x01\x01\x02\x57', rlp.encode(['jimbojones']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
branch_node = state._decode_to_node(state.root_node[1])
print 'banch is:', branch_node
next_hash = branch_node[5]
print 'hash stored in branch node:', next_hash.encode('hex')
print 'branch node it points to:', state._decode_to_node(next_hash)
print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'

print rlp.decode(state.get('\x01\x01\x02'))
print rlp.decode(state.get('\x01\x01\x02\x55'))
print rlp.decode(state.get('\x01\x01\x02\x57'))