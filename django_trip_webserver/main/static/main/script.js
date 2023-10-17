// 모든 SVG 요소의 title을 찾아 말풍선 스타일링을 적용
document.querySelectorAll('svg a title').forEach(function(title) {
    title.classList.add('tooltip');
});
