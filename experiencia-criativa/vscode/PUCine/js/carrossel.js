var currentImage = 0;
var previousImage = 2;
var nextImage = 1;

$('.bolinha').click(function() {
  var targetImage = $(this).index();
  
  // Atualiza as variáveis de imagem
  previousImage = currentImage;
  currentImage = targetImage;
  nextImage = targetImage == 2 ? 0 : targetImage + 1;

  // Atualiza as imagens
  $('.carrossel img').eq(previousImage).css('transform', 'translateX(-100%)');
  $('.carrossel img').eq(currentImage).css('transform', 'translateX(0)');
  $('.carrossel img').eq(nextImage).css('transform', 'translateX(100%)');
})