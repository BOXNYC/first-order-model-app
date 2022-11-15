# pip install imageio
# pip install path.py
# pip install ffmpeg
# pip install torchvision==0.5
# pip install torch==1.4
# pip install opencv-python
# pip install scikit-image==0.17.2
# pip install imageio_ffmpeg
# pip install tensorflow==2.6.0
# pip install pandas
# pip install numpy==1.20.3

rm -rf first_order_model
git clone https://github.com/BOXNYC/first-order-model first_order_model
rm -rf sample_data
cp begin.py first_order_model/begin.py
cd first_order_model
mkdir frames

# Git
wget https://github.com/Warhawk947/DameDaneGenerator/releases/download/1/vox-cpk.pth.tar -O vox-cpk.pth.tar
wget https://raw.githubusercontent.com/davisking/dlib-models/master/shape_predictor_68_face_landmarks.dat.bz2 -O shape_predictor_68_face_landmarks.dat.bz2

# Google Drive
# wget https://github.com/Warhawk947/DameDaneGenerator/releases/download/1/vox-cpk.pth.tar -O vox-cpk.pth.tar
# wget https://raw.githubusercontent.com/davisking/dlib-models/master/shape_predictor_68_face_landmarks.dat.bz2 -O shape_predictor_68_face_landmarks.dat.bz2

git clone https://github.com/BOXNYC/first-order-model-align.git
rm -rf align/\.git
mv align/* .
rm -rf align

## FOR DEV ONLY: 
chown joseph:joseph begin.py
