function handleLike() {
  var likeButton = document.getElementById("like-button");
  var dislikeButton = document.getElementById("dislike-button");
  var videoId = likeButton.getAttribute("video-id");
  var userId = likeButton.getAttribute("user-id");

  if (!userId) {
    //User is not logged in, redirect to the login page
    window.location.href = "/login";
    return;
  }

  //Check if the like button is already active
  if (likeButton.classList.contains("active")) {
    //User wants to undo the like action
    likeButton.classList.remove("active");

    handleRemove(videoId, userId, 1);

    return;
  }

  //Check if the dislike button is active
  if (dislikeButton.classList.contains("active")) {
    //User wants to change from like to dislike
    dislikeButton.classList.remove("active");

    handleToggle(videoId, userId, -1);

    //Update UI
    likeButton.classList.add("active");

    return;
  }

  //Set the like button as active
  likeButton.classList.add("active");

  //Send request to update the database (add the like reaction)
  fetch("/like", {
    method: "POST",
    body: new URLSearchParams({
      video_id: videoId,
      user_id: userId,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}

function handleDislike() {
  var dislikeButton = document.getElementById("dislike-button");
  var likeButton = document.getElementById("like-button");
  var videoId = dislikeButton.getAttribute("video-id");
  var userId = dislikeButton.getAttribute("user-id");

  if (!userId) {
    //User is not logged in, redirect to the login page
    window.location.href = "/login";
    return;
  }

  //Check if the dislike button is already active
  if (dislikeButton.classList.contains("active")) {
    //User wants to undo the dislike action
    dislikeButton.classList.remove("active");

    handleRemove(videoId, userId, -1);

    return;
  }

  //Check if the like button is active
  if (likeButton.classList.contains("active")) {
    //User wants to change from like to dislike
    likeButton.classList.remove("active");

    handleToggle(videoId, userId, 1);

    //Update UI
    dislikeButton.classList.add("active");

    return;
  }

  //Set the dislike button as active
  dislikeButton.classList.add("active");

  //Send request to update the database (add the dislike reaction)
  fetch("/dislike", {
    method: "POST",
    body: new URLSearchParams({
      video_id: videoId,
      user_id: userId,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}

function handleRemove(videoId, userId, current_reaction) {
  //Send request to update the database (remove the current reaction)
  fetch("/remove_reaction", {
    method: "PATCH",
    body: new URLSearchParams({
      video_id: videoId,
      user_id: userId,
      current_reaction: current_reaction,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}

function handleToggle(videoId, userId, current_reaction) {
  //Send request to update the database (toggle current reaction)
  fetch("/toggle_reaction", {
    method: "PATCH",
    body: new URLSearchParams({
      video_id: videoId,
      user_id: userId,
      current_reaction: current_reaction,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}
