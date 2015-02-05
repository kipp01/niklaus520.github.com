{% if theme.jquery || theme.fancybox %}
  <script type="text/javascript" src="{{ url_for(theme.vendors) }}/jquery/dist/jquery.min.js"></script>
{% endif %}

{% if theme.fancybox %}
  <script type="text/javascript" src="{{ url_for(theme.vendors) }}/fancybox/source/jquery.fancybox.pack.js"></script>
  <script type="text/javascript">
    $(document).ready(function() {
      $(".fancybox").fancybox();
    });
  </script>
{% endif %}

{% if theme.duoshuo and theme.duoshuo.enable and theme.duoshuo.shortname %}
  <script type="text/javascript">
    var duoshuoQuery = {short_name:"{{config.duoshuo.shortname}}"};
    (function() {
      var ds = document.createElement('script');
      ds.type = 'text/javascript';ds.async = true;
      ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
      ds.charset = 'UTF-8';
      (document.getElementsByTagName('head')[0]
      || document.getElementsByTagName('body')[0]).appendChild(ds);
    })();
  </script>
{% endif %}

{% if theme.google_analytics %}
    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', '{{ theme.google_analytics }}', 'auto');ga('send', 'pageview');
    </script>
{% endif %}

<script type="text/x-mathjax-config"> 
MathJax.Hub.Config({ 
      tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]} 
}); 
</script>
<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

