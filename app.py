import os
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaRecorder

ROOT = os.path.dirname(__file__)
RECORDING_DIR = os.path.join(ROOT, "recordings")
os.makedirs(RECORDING_DIR, exist_ok=True)

pcs = set()

async def index(request):
    return web.FileResponse(os.path.join(ROOT, 'static/index.html'))

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params['sdp'], type=params['type'])

    pc = RTCPeerConnection()
    pcs.add(pc)

    recorder = MediaRecorder(os.path.join(RECORDING_DIR, 'output.wav'))

    @pc.on('track')
    def on_track(track):
        print(f'Track recebida: {track.kind}')
        recorder.addTrack(track)

        @track.on('ended')
        async def on_ended():
            print('Parando gravação...')
            await recorder.stop()

    await pc.setRemoteDescription(offer)
    await recorder.start()
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.json_response({
        'sdp': pc.localDescription.sdp,
        'type': pc.localDescription.type
    })

# App e rotas
app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/offer', offer)
app.router.add_static('/static/', path=os.path.join(ROOT, 'static'), name='static')

# Iniciar servidor
web.run_app(app, host='0.0.0.0', port=8080)
