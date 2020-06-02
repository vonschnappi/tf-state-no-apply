import json
import sys

resources = json.loads(open(sys.argv[1], 'r').read())
tf_state = json.loads(open(sys.argv[2], 'r').read())

tf_state['resources'] = resources

with open(sys.argv[2], 'w') as fp:
    json.dump(tf_state, fp, indent=4)
