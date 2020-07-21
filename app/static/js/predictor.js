// UI js start
function readURL(input) {
    // Clear label
    document.getElementById("label-container").innerHTML = "";

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
            $('.image-upload-wrap').hide();

            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();

            $('.image-title').html(input.files[0].name);
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}

$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});
// UI js end
// AI core start
// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

const LABEL_CLASS = ["bg-danger", "bg-success", "bg-warning", "bg-info"];

// the link to your model provided by Teachable Machine export panel
const URL = "/static/model/";

let model, labelContainer, maxPredictions;

// Load the image model and setup the webcam
async function init() {
    showLoader();

    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";
    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();
    labelContainer = document.getElementById("label-container");

    hideLoader();
}

// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
    const image = document.getElementById("face-image");
    if (image == null) {
        alert("Please select image.");
        return;
    }

    labelContainer.innerHTML = "";

    const prediction = await model.predict(image, false);
    for (let i = 0; i < maxPredictions; i++) {
        labelContainer.innerHTML += '<div>' + prediction[i].className + '</div>';
        labelContainer.innerHTML += '<div class=\"progress\">'
            + '<div class=\"progress-bar ' + LABEL_CLASS[i] + '\"'
            + ' role=\"progressbar\" '
            + ' style=\"width: ' + prediction[i].probability.toFixed(2) * 100 + '%\"'
            + ' aria-valuenow=\"' + prediction[i].probability.toFixed(2) * 100 + '\" aria-valuemin=\"0\" aria-valuemax=\"100\">'
            + prediction[i].probability.toFixed(2) * 100 + '%'
            + '</div>'
            + '</div>';
    }
}

function showLoader() {
    $("body").addClass("hide-scroll");
    $(".global-loader-mask").css("display", "flex");
}

function hideLoader() {
    $("body").removeClass("hide-scroll");
    $(".global-loader-mask").css("display", "none");
}

// AI core end
// API start
$(document).ready(function () {
    $("#predict-image-url-form").submit(function (e) {
        e.preventDefault();

        let data = JSON.stringify({
            url: $("#url").val()
        });


        showLoader();
        renderJson($("#predict-image-url-result"), "{}");
        $.ajax({
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            url: "/xeye/predict/url",
            data: data,
            success: function (response, status, xhr) {
                let result = JSON.stringify(response);
                renderJson($("#predict-image-url-result"), result);
            },
            error: function (jqXhr, textStatus, errorMessage) {
                let result = JSON.stringify(jqXhr.responseText);
                renderJson($("#predict-image-url-result"), result);
            },
            complete: function () {
                hideLoader();
            }
        })
    });

    $("#predict-upload-image").change(function () {
        predictorUploadImage();
    });

    $("#predict-upload-image-form").submit(function (e) {
        e.preventDefault();
        predictorUploadImage();
    });

    function predictorUploadImage() {
        let data = new FormData();
        data.append('file', $("#predict-upload-image")[0].files[0]);

        showLoader();
        renderJson($("#predict-upload-image-result"), "{}");
        $.ajax({
            type: "POST",
            url: "/xeye/predict/file",
            data: data,
            dataType: 'json',
            contentType: false,
            processData: false,
            success: function (response, status, xhr) {
                let result = JSON.stringify(response);
                renderJson($("#predict-upload-image-result"), result);
            },
            error: function (jqXhr, textStatus, errorMessage) {
                let result = JSON.stringify(jqXhr.responseText);
                renderJson($("#predict-upload-image-result"), result);
            },
            complete: function () {
                hideLoader();
            }
        });
    }

    function renderJson(element, response) {
        try {
            let input = eval("(" + response + ")");
            let options = {
                collapsed: false,
                rootCollapsable: false,
                withQuotes: true,
                withLinks: false
            };

            element.jsonViewer(input, options);
        } catch (error) {
            return alert("Cannot eval JSON: " + error)
        }
    }
});
// API end
