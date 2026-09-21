// I barely know javascript but I do understand basic stuff
// Since js does not have a direct equalvilant to the random.choice() method
// in python, we gotta get a random choice by generating a random number from the
// length of an array, which can then be used to refer to the option using indexing

// I promise you i'm not completely stupid and that im not just vibecoding some ai
// bs here. This dumbass code is 100% human written.

// Keeping it simple by copying some basic code that wraps 
// an audio source into a function callable by a button


/*function song_randomizer*/

/* Initialize music as an audio object*/

function initMusic(){
	const songs = ["/assets/sounds/concussion.mp3", "/assets/sounds/away.mp3", "/assets/sounds/higher_thinking.mp3"];
	const randSongIndex = Math.floor(Math.random() * songs.length);
	const randSong = songs[randSongIndex];
	console.log("Randomly selected song:");
	console.log(randSong);
	music = new Audio(randSong);
}

initMusic();
// Call function to initialize variables

// Play music from the music button
function musicButton(){
	if (music.paused !== true){
		music.pause();
		initMusic();
	}else{
		music.play();
	    }

}

/* call button when script loads to autoplay music. 
 * falls back to being called manually by an htmlbutton when autoplay isnt allowed.*/

musicButton();
