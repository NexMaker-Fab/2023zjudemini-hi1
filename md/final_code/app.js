const video = document.getElementById('video');
const outputElem = document.getElementById('output');

async function setupCamera() {
    video.width = 1000;
    video.height = 800;
    const stream = await navigator.mediaDevices.getUserMedia({ 'video': true });
    video.srcObject = stream;
    video.style.transform = "scaleX(-1)";

    return new Promise((resolve) => {
        video.onloadedmetadata = () => {
            resolve(video);
        };
    });
}

async function bindPoseDetectionFrame() {
    const model = poseDetection.SupportedModels.MoveNet;
    const detector = await poseDetection.createDetector(model);
    let poses = [];

    video.play();

 // 姿态检测功能
async function detectPoses() {
    // 这将使用当前视频帧进行姿态估计
    const poses = await detector.estimatePoses(video);
    outputElem.textContent = JSON.stringify(poses, null, 2);
    // 更新您想要发送到服务器的变量
    window.latestPoses = poses;
    // 继续下一帧的姿态检测
    requestAnimationFrame(detectPoses);
}

// 数据上传功能
function uploadPoses() {
    // 检查是否有最新的姿态数据
    if (window.latestPoses) {
        fetch('http://localhost:5000/upload_pose_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(window.latestPoses),
        })
        .then(response => response.json())  // 转换响应为JSON
        .then(data => {
            console.log('Server response:', data);
        })
        .catch(error => {
            console.error('Error sending poses:', error);
        });
    }
}

// 初始化姿态检测
detectPoses();

// 每2秒上传一次数据
setInterval(uploadPoses, 2000);
}

async function bindPage() {
    await setupCamera();
    video.play();
    bindPoseDetectionFrame();
}

window.onload = bindPage;
