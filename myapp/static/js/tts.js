function speak(text){
	fetch("/myapp/ai_speech/", {
		method: "POST",
		headers: { "Content-Type": "application/x-www-form-urlencoded" },
		body: "text=" + encodeURIComponent(text)
	})
	.then(response => response.text())
	.then(data => console.log("TTS:", data))
	.catch(err => console.error("TTS:", err));
}

