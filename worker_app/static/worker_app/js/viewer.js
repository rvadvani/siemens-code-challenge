document.addEventListener('DOMContentLoaded', function() {
    const fileList = document.getElementById('file-list');
    const fileViewer = document.getElementById('file-viewer');

    
    fetch('/api/files')
        .then(response => response.json())
        .then(files => {
            files.forEach(file => {
                const button = document.createElement('button');
                button.classList.add('btn');
                button.textContent = file;
                // console.log("file name & format: ", file, file.split('.').pop())
                button.onclick = () => loadFile(file);
                fileList.appendChild(button);
            });
        });

    
    function loadFile(file) {
        fileViewer.src = `/api/file/${file}`;
    }
});
