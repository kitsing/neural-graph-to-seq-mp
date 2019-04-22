import sys, os, json

amr = [x.strip() for x in open(sys.argv[1]+'.amr','rU')]
print 'len(amr)', len(amr)
sent = [x.strip() for x in open(sys.argv[1]+'.sen','rU')]
print 'len(sent)', len(sent)
assert len(amr) == len(sent)

ids = None
if os.path.isfile(sys.argv[2]):
    ids = [x.strip() for x in open(sys.argv[2],'rU')]
    assert len(amr) == len(ids)

data = []
for i in range(len(amr)):
    json_obj = {'amr':amr[i],'sent':sent[i],}
    if ids != None:
        json_obj['id'] = ids[i]
    data.append(json_obj)
print len(data)
json.dump(data,open(sys.argv[1]+'.json','w'))

