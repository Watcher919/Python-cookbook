=========================================================
��Python Cookbook 3rd Edition�� ���� 
=========================================================

�սӴ�����Python Cookbook 3rd Edition���Ȿ��ʱ������û����Ӧ�����İ档
���Ķ��Ȿ��ʱ��ͻȻ�뵽��Ϊʲô�������������Ҳ��������Ķ��أ����Ǿ������Ķ�ʱ���µط����Ȿ�顣
�ⲻ��һ�����ɵĹ�����ȴ��һ��ֵ�����Ĺ��������������˱��ˣ����Ҷ��Լ���������Ҳ��һ�ֶ�����������

���������£�һ���˱Ͼ��������ޡ�����ܷŵ�github���������һ��������룬��Ч������ȫ��һ���ˡ�
ϣ���Ȱ�python����־֮ʿ����һ��������Ȿ�鷭����ɡ�ͨ��fork/pull request��ʽ������һ�Ѻ�����������
�����Ȿ���ǰ���Ƕ�python����Ҫ���൱������о����벻Ҫʹ��google���������Ĺ��ߣ�
��Ҫ�ܰ�ԭ�����ߵ���˼��ȫ������������Ҫ���ַ��룬������һ��Ҫ׼ȷ��

�����ڷ���ʱ��ѭһ��ԭ�򣬾���ͨ�����ġ�Python3.4.0�û��ֲᡷ����ȫ�������ֺʹ�����ٷ��룬
�����ǽ����������ַ��룬�������������Ҫ������˼����ӽӽ����Ҹ���������⡣
ԭ������֮ǰ�������߼���������Щ�����Ķ�û����������Ϣ�������һ�·�����ɺ��ٷ��벹�롣

Ŀǰ�����˵�һ�¡������ݽṹ���㷨 ���о��������Python��׼��һ����֪��
��������������ס����Խ��������Ķ�ʱ�����Ҳ�˽�һ���ֲ�����صĵط���

��������ʲô��©�ĵط����Ҽ��£�Ҳ��ӭ���ָ���� yidao620@gmail.com

--------------------------------------------------------------

ע��

1. �����ĵ���ʹ��reStructuredText�༭���ο� reStructuredText_
2. ��ǰ�ĵ������й��� readthedocs_ ��
3. ʹ����python�ٷ��ĵ����� sphinx-rtd-theme_ ��Ĭ��theme��default���õľ������.

::

    # on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

    if not on_rtd:  # only import and set the theme if we're building docs locally
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    # otherwise, readthedocs.org uses their theme by default, so no need to specify it

.. _readthedocs: https://readthedocs.org/
.. _sphinx-rtd-theme: https://github.com/snide/sphinx_rtd_theme
.. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html