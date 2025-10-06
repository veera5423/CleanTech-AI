// CleanTech - JavaScript Enhancements

// Image preview on file select
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const preview = document.getElementById('image-preview');

    if (fileInput && preview) {
        fileInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.classList.remove('d-none');
                    preview.classList.add('d-block');
                };
                reader.readAsDataURL(file);
            } else {
                preview.classList.remove('d-block');
                preview.classList.add('d-none');
            }
        });
    }
});
