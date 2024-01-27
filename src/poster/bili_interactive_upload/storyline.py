import json
import exrrx
import time
import networkx
import random
sysrand=random.SystemRandom()
# can you just parse and replace?

def mima_int(_mi,_ma):
    assert type(_mi)==int
    assert type(_ma)==int
    assert _mi<_ma
    return sysrand.choice(list(range(_mi,_ma+1)))
def now():
    return round(time.time()*1000)
def gen_link():
    return exrex.getone("l-[0-9a-zA-Z#@]{10}")
def gen_var():
    return exrex.getone("v-[0-9a-zA-Z#@]{10}")
def gen_node():
    return exrex.getone("n-[0-9a-zA-Z#@]{9}")
def rtheme():
    return mima_int(1,11) 
class story:
    def __init__(self,graph):
        self.graph=graph
        self.vlist=
        self.nlist=
        self.llist=
    def init_names(self):
# the hash is generated from [vl]-[0-9a-zA-Z#@]{10}, n-[0-9a-zA-Z#@]{9}.
# variable value ranging from 0 to 100.
# if we want to be some copycat then it is just fine.
# branching node -> flowLink -> virtual node -> refLink -> jump target
# the cropping method shall be applied on the cover image.
# ratio is 960:600.
# it should be conversion instead of something else.
"""
graph(dict) -> script (escaped \" JSON string) -> hasGoto true
                                               -> editorVersion "1.4.6"
                                               -> createdTime 1607968436531 (using Date.now())
                                               -> currentThemeId 11 (button theme)
                                               -> enableVariables true
                                               -> nodes (dict) -> n-U9IKgqOwz -> id "n-U9IKgqOwz"
                                                                              -> type "videoNode/gotoNode" (gotoNode has empty data dict)
                                                                              -> data (dict) -> type 0/1/2 (0-NODE_TYPE_PLAY, 1-NODE_TYPE_SELECT 2-NODE_TYPE_POINT)
                                                                                             -> aid ""
                                                                                             -> cid <video_cid>
                                                                                             -> name "nodename"
                                                                                             -> duration <duration in miliseconds>
                                                                                             -> index 1 (the P_ number)
                                                                                             -> showTime 0/5 (how many seconds shall options appear, 0 for infinite)
                                                                                             -> innerOptions [] (not to fuck with it)
                                                                                             -> dimension (dict) -> width <video_width>
                                                                                                                 -> height <video_height> (seems to follow 1920*1080, especially 1080)
                                                                              -> isRoot true
                                                                              -> input [] (from flowLink)
                                                                              -> output ["l-9wPBhA3DYG","l-Ku7rG1F5Uy","l-@rsVvtjRtA"] (gotoNode can only have one, videoNode 4)
                                                                              -> refInput [] (from reflink)
                                                                              -> refOutput [] (only for gotoNode)
                                               -> links (dict) -> l-9wPBhA3DYG (dict) -> id "l-9wPBhA3DYG"
                                                                                      -> type "flowLink/reflink" (reflink can jump around except for the "from" node or the virtual node, and have empty data dict)
                                                                                      -> data (dict) -> id "l-9wPBhA3DYG"
                                                                                                     -> text "a jumplink"
                                                                                                     -> default true
                                                                                                     -> point (dict) -> x 0 (range (0,1), leave 0 for assignments later) 
                                                                                                                     -> y 0
                                                                                                                     -> align 2 (what is this align?)
                                                                                                     -> conditions (controlling to appear this one or not) [{"vid":"v-6ztcnfk9bz","type":"ge/gt/le/lt/eq","value":0,"value2":100,"enabled":false}, (value2 must be greater than value)
                                                                                                                    {"vid":"v-3pihLg1zJY","type":"range","value":1,"value2":100,"enabled":false}] (only useful when type is "range")
                                                                                                     -> actions (after selection) [{"vid":"v-mJe1rMDpb","type":"add/sub/assign","value":0,"enabled":true}]
                                                                                      -> from: "n-U9IKgqOwz"
                                                                                      -> to: "n-aO0f9zG6l"
                                               -> variables [] -> (dict) -> v-@5Cni3WYlG
                                                                         -> type 1/2 (1 for variable, 2 for random)
                                                                         -> name "数值3" 
                                                                         -> initValue 5
                                                                         -> initValue2 0 (for random variable,if so must be greater than initValue)
                                                                         -> displayable false (to hide it or not)
            -> aid <av_id>
            -> skin_id <skin_id>
            -> nodes [] -> (dict) -> id "<node_id>" (only for videoNode)
                                  -> cid <cid>
                                  -> name <node_name>
                                  -> is_start 1/0 (i for initial node, 0 for childrens)
                                  -> show_time -1 (-1 for infinite, anything other than that means the option duration)
                                  -> otype 1/2 (1 for auto align options, 2 for pinpoint options) 
                                  -> edges [] -> (dict) -> id "<edge_id>" (flowLink)
                                                        -> title "edge title"
                                                        -> to_node_id "<dest_node_id>" (must be videoNode)
                                                        -> is_default 0/1 (1 for default)
                                                        -> condition [] -> (dict) -> var_id "v-3pihLg1zJY" (this can be used multiple times for same var to produce "reign" effect)
                                                                                  -> condition "le/lt/ge/gt/eq"
                                                                                  -> value 0
                                                        -> attribute [] -> (dict) -> var_id "<var_id>" (cannot be random variable)
                                                                                  -> action "add/sub/assign"
                                                                                  -> value 0
                                                        -> text_align (top:1 right:2 bottom:3 left:4) (for otype:2)
                                                        -> pos_x <abs_pos_x> (for otype:2)
                                                        -> pos_y <abs_pos_y> (for otype:2)
            -> regional_vars [] -> (dict) -> name: "<number_name>"
                                          -> init_min initValue
                                          -> init_max initValue2
                                          -> type 1/2 (1 for variable, 2 for random)
                                          -> id "<variable_id>"
                                          -> is_show 0/1 (0 for not show, 1 for show)
"""
# just WTF?
# main issues: convert what to what?
# better use a unified framework or not.
