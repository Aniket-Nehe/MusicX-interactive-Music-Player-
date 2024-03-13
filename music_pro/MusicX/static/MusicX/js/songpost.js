const track = document.getElementById('track');
const play = document.getElementById('play');
const pause = document.getElementById('pause');
const prevTrack = document.getElementById('prev-track');
const nextTrack = document.getElementById('next-track');
const thumbnail = document.getElementById('thumbnail');
const trackInfo = document.querySelector('.track-info');
const trackTitle = document.getElementById('track-title');
const trackArtist = document.getElementById('track-artist');
const progressBar = document.getElementById('progressBar');
const currentTime = document.getElementById('currentTime');
const durationTime = document.getElementById('durationTime');

let isPlaying = false;
let currentTrack = 0;

// Function to update the track info
function updateTrackInfo() {
  trackTitle.innerText = songs[currentTrack].name;
  trackArtist.innerText = songs[currentTrack].singer;
  thumbnail.src = `/media/${songs[currentTrack].image}`;
  track.src = `\media\${songs[currentTrack].Song}`;
}

// Function to update the progress bar
function updateProgressBar(e) {
  const { duration, currentTime } = e.target;
  const progressPercent = (currentTime / duration) * 100;
  progressBar.value = progressPercent;
  currentTime.innerText = formatTime(currentTime);
}

// Function to update the duration time
function updateDurationTime(e) {
  const { duration } = e.target;
  durationTime.innerText = formatTime(duration);
}

// Function to format the time
function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const secondsLeft = Math.floor(seconds % 60);
  return `${minutes}:${secondsLeft < 10 ? '0' + secondsLeft : secondsLeft}`;
}

// Function to play the track
function playTrack() {
  track.play();
  isPlaying = true;
  play.style.display = 'none';
  pause.style.display = 'block';
}

// Function to pause the track
function pauseTrack() {
  track.pause();
  isPlaying = false;
  play.style.display = 'block';
  pause.style.display = 'none';
}

// Function to play the next track
function nextTrackFunc() {
  currentTrack++;
  if (currentTrack >= songs.length) {
    currentTrack = 0;
  }
  updateTrackInfo();
  playTrack();
}

// Event listeners
play.addEventListener('click', playTrack);
pause.addEventListener('click', pauseTrack);
prevTrack.addEventListener('click', () => {
  currentTrack--;
  if (currentTrack < 0) {
    currentTrack = songs.length - 1;
  }
  updateTrackInfo();
  playTrack();
});
nextTrack.addEventListener('click', nextTrackFunc);
track.addEventListener('timeupdate', updateProgressBar);
track.addEventListener('loadedmetadata', updateDurationTime);

// Initialize the track info
updateTrackInfo();