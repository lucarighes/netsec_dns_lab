from flask import Flask

app = Flask("trusted")

@app.route('/', methods=['GET'])
def start_attack():
	toRtn = """
*Here is the malicous webserver with IP: 192.168.0.151*

                    uuuuuuuu
                 uu$$$$$$$$$$$uu
              uu$$$$$$$$$$$$$$$$$uu
             u$$$$$$$$$$$$$$$$$$$$$u
            u$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$*   *$$$*   *$$$$$$u
           *$$$$*      u$u       $$$$*
            $$$u       u$u       u$$$
            $$$u      u$$$u      u$$$
             *$$$$uu$$$   $$$uu$$$$*
              *$$$$$$$*   *$$$$$$$*
                u$$$$$$$u$$$$$$$u
                 u$*$*$*$*$*$*$u
    uuu          $$u$ $ $ $ $u$$         uuu
     u$$$$        $$$$$u$u$u$$$       u$$$$
      $$$$$uu      *$$$$$$$$$*     uu$$$$$$
    u$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$$
    $$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
     ***      **$$$$$$$$$$$uu **$***
               uuuu **$$$$$$$$$$uuu
     u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
      $$$$$$$$$$****           **$$$$$$$$$$$*
       *$$$$$*                      **$$$$**
         $$$*                         $$$*
"""
	return toRtn



if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 80)
