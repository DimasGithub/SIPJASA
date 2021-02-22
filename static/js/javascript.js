
// data tables
$(document).ready( function () {
    $('table.table').DataTable();
} );



// modal delete confirm  
$(document).on('click', '.confirm-delete', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmDeleteButtonModal', function () {
  var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});



//modal received confirm
$(document).on('click', '.confirm-received', function () {
  $("#confirmReceivedModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmReceivedButtonModal', function () {
  var caller = $("#confirmReceivedButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});



//modal rejected confirm
$(document).on('click', '.confirm-rejected', function () {
  $("#confirmRejectedModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmRejectedButtonModal', function () {
  var caller = $("#confirmRejectedButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});



//modal banned confirm
$(document).on('click', '.confirm-banned', function () {
  $("#confirmBannedModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmBannedButtonModal', function () {
  var caller = $("#confirmBannedButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});



// modal process confirm
$(document).on('click', '.confirm-processed', function () {
  $("#confirmProcessedModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmProcessedButtonModal', function () {
  var caller = $("#confirmProcessedButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});



//modal finish confirm
$(document).on('click', '.confirm-finish', function () {
  $("#confirmFinishModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmFinishButtonModal', function () {
  var caller = $("#confirmFinishButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});

