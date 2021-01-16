$form = $('form')
console.log($form)

class BoggleGame {
  /* make a new game at this DOM id */

  constructor(boardId, time=60) {
    this.score = 0;
    this.words = new Set();
    this.board = $("#" + boardId);
    $(".submit-word").on("submit", this.handleSubmit.bind(this));
    this.form = $('form')
    this.guesses = []

    this.time = time
    // every sec, tick down one second
    this.timer = setInterval(this.tick.bind(this), 1000);
  }

  /* show word in list of words */
  showWord(word) {
    $("#words").prepend($("<li>", { text: word }));
  }

  /* show score in html */
  showScore(word) {
    let wordScore = word.length
    this.score += wordScore
    $("#score").text(this.score)
  }

  /* show a status message */
  showMessage(msg) { 
    $("#message-text").text(msg)
  }
  
  /* handle submission of word: if unique and valid, score & show message`*/
  async handleSubmit(evt) {
    evt.preventDefault();
    
    const $word = $("#word");

    let word = $word.val();
    if (!word) return;
    if (this.guesses.includes(word)) {
      this.showMessage("Try a new word")
      return
    }
    // check server for validity
    const resp = await axios.get("/check-word", { params: { word: word }});
    
    if (resp.data.result === "not-word") {
      this.showMessage(`${word} not valid`);
    } else if (resp.data.result === "not-on-board") {
      this.showMessage(`${word} not on board`);
    } else {
      this.showWord(word);
      this.showMessage(`Added: ${word}`);
      this.showScore(word);
      this.guesses.push(word)
    }

    evt.preventDefault()
  }

  /* Update timer in DOM */
  showTimer() {
    $(".timer").text(this.time);
  }
  hideTimer() {
    $("#timer-row").hide()
    $("#word").hide()
    $("form").hide()
    $("#message-text").hide()
  }


  /* Tick: handle a second passing in game */
  async tick() {
    this.time -= 1;
    this.showTimer();
    if (this.time === 0) {
      alert(`time's up. Your Final Score: ${this.score}`)
      this.hideTimer()
    }
  }

  async scoreGame() {
    const resp = await axios.post("/post-score", { score: this.score });
    if (resp.data.brokeRecord) {
      this.showMessage(`New record: ${this.score}`, "ok");
    } else {
      this.showMessage(`Final score: ${this.score}`, "ok");
    }
  }


}


