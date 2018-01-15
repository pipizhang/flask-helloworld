from .os import top

def mtop():
    return "<html style=\"background:black;color:white\"><meta http-equiv=\"refresh\" content=\"5\"><pre>"+top()+"</pre></html>"

