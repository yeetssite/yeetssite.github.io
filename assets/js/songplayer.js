// I barely know javascript but I do understand basic stuff
// Since js does not have a direct equalvilant to the random.choice() method
// in python, we gotta get a random choice by generating a random number from the
// length of an array, which can then be used to refer to the option using indexing

// I promise you i'm not completely stupid and that im not just vibecoding some ai
// bs here. This dumbass code is 100% human written.
const songs = ["../sounds/concussion.mp3", "../sounds/away.mp3", "../sounds/higher_thinking.mp3"];
const randSongIndex = Math.floor(Math.random() * songs.length);
const randSong = songs[randSongIndex];
console.log("Randomly selected song:");
console.log(randSong);

// Keeping it simple by copying some basic code that wraps 
// an audio source into a function callable by a button
function playMusic() {
	var music = new Audio("../sounds/concussion.mp3");
	music.play();
}
