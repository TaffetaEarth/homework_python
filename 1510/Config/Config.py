import configparser
f = open("config.cfg", "r")
cfg = configparser.ConfigParser()
cfg.read('config.cfg')
g = cfg['file']['text']
old = cfg['word_to_replace']['replaced_word']
new = cfg['new_word']['new_word']
fn = open(g, 'r').read().replace(old, new)
f.close()
f = open(g, 'w')
f.write(fn)
