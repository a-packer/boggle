class BoggleGame {
  /* make a new game at this DOM id */

  constructor(boardId) {

    this.score = 0;
    this.words = new Set();
    this.board = $("#" + boardId);
    $(".submit-word").on("submit", this.handleSubmit.bind(this));
  }

  /* show word in list of words */
  showWord(word) {
    $("#words", this.board).append($("<li>", { text: word }));
  }

  /* show score in html */
  showScore() {
  }

  /* show a status message */
  showMessage(msg, cls) {
    $("#message-text", this.board).text(msg)
  }

  /* handle submission of word: if unique and valid, score & show message`*/
  async handleSubmit(evt) {
    evt.preventDefault();
    const $word = $("#word", this.board);

    let word = $word.val();
    if (!word) return;

    // check server for validity
    const resp = await axios.get("/check_word", { params: { word: word }});
    if (resp.data.result === "not-word") {
      this.showMessage(`${word} is not a valid English word`, "err");
    } else if (resp.data.result === "not-on-board") {
      this.showMessage(`${word} is not a valid word on this board`, "err");
    } else {
      this.showWord(word);
    }
  }

}