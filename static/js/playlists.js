function handleAddtoPL() {
  var plButton = document.getElementById("add-to-pl-button");
  var videoId = plButton.getAttribute("video-id");
  var userId = plButton.getAttribute("user-id");

  if (!userId) {
    //User is not logged in, redirect to the login page
    window.location.href = "/login";
    return;
  }
  //Mark the button as active so that it's appearance changes
  if (plButton.classList.contains("active")) {
    plButton.classList.remove("active");

    handleRemoveFromPL(userId, videoId);

    return;
  }

  plButton.classList.add("active");

  //Request to server to add a video to playlist
  fetch("/add_to_playlist", {
    method: "POST",
    body: new URLSearchParams({
      user_id: userId,
      video_id: videoId,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}

function handleRemoveFromPL(userId, videoId) {
  //Request to server to remove a video from playlist
  fetch("/remove_from_playlist", {
    method: "POST",
    body: new URLSearchParams({
      user_id: userId,
      video_id: videoId,
    }),
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error("Error:", error);
    });
}
