from flask import Flask, render_template_string
app = Flask(__name__)

H = """
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
 body{font-family:sans-serif;background:#f5f5f5;display:flex;justify-content:center;padding:20px;margin:0}
 .card{background:white;padding:20px;border-radius:15px;width:100%;max-width:350px;box-shadow:0 2px 10px rgba(0,0,0,0.05);margin-top:20px;text-align:center}
 .header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
 .logo{color:#4285f4;font-weight:bold;font-size:24px}
 .bar-c{flex-grow:1;background:#eee;height:8px;border-radius:10px;margin:0 15px}
 .bar{background:#34a853;height:100%;border-radius:10px;transition:0.3s}
 .step{display:none} .active{display:block}
 hr{border:0;border-top:1px solid #eee;margin:15px 0}
 .question{font-weight:bold;font-size:18px;margin-bottom:20px;text-align:left}
 .opt{display:block;text-align:left;margin:12px 0;font-size:16px;cursor:pointer}
 input{transform:scale(1.3);margin-right:10px}
 .btn{width:100%;background:#4285f4;color:white;border:none;padding:15px;border-radius:10px;font-weight:bold;margin-top:10px;cursor:pointer}
</style></head>
<body><div class="card">
 <div class="header"><span class="logo">ypolls</span><div class="bar-c"><div id="pb" class="bar" style="width:33%"></div></div><span id="pt">33%</span></div><hr>

 <div id="s1" class="step active">
  <div class="question">1. B?QuC) plataforma de streaming consumes?</div>
  <label class="opt"><input type="checkbox"> Netflix</label>
  <label class="opt"><input type="checkbox"> Disney+</label>
  <label class="opt"><input type="checkbox"> HBO Max</label>
  <button class="btn" onclick="go(1,2,66)">Siguiente</button>
 </div>

 <div id="s2" class="step">
  <div class="question">2. B?QuC) marcas ve en publicidad?</div>
  <label class="opt"><input type="checkbox"> Mercado Libre</label>
  <label class="opt"><input type="checkbox"> Toyota Motor</label>
  <label class="opt"><input type="checkbox"> Amazon</label>
  <button class="btn" onclick="go(2,3,90)">Siguiente</button>
 </div>

 <div id="s3" class="step">
  <div class="question">3. B?QuC) productos consumes habitualmente?</div>
  <label class="opt"><input type="checkbox"> Coca-Cola Corp</label>
  <label class="opt"><input type="checkbox"> Pepsi .org</label>
  <label class="opt"><input type="checkbox"> Nestel</label>
  <button class="btn" onclick="go(3,4,100)">Finalizar</button>
 </div>

 <div id="s4" class="step">
  <h2 style="color:#34a853">B!Gracias!</h2>
  <p>Has terminado la encuesta de ypolls correctamente.</p>
  <button class="btn" style="background:#666" onclick="window.location.href='https://google.com'">Salir</button>
 </div>
</div>
<script>
 function go(a,b,p){
  document.getElementById('s'+a).style.display='none';
  document.getElementById('s'+b).style.display='block';
  document.getElementById('pb').style.width=p+'%';
  document.getElementById('pt').innerText=p+'%';
 }
</script></body></html>
"""

from flask import request

@app.route('/')
def home():
    # Obtiene la IP real saltando el proxy de Render
    ip_addr = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Imprime el log en la consola de Render
    print(f"\n--- LOG DE ACCESO ---")
    print(f"IP: {ip_addr}")
    print(f*****************\n")
    
    return render_template_string(H)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

