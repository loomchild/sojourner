from distutils.core import setup
from sojourner import VERSION

setup(
    name='Sojourner',
    version=VERSION,
    description='Conference schedule application for the Nokia N900',
    author='Will Thompson',
    url='https://github.com/loomchild/sojourner',
    packages=['sojourner'],
    scripts=['bin/sojourner'],
    data_files=[
        ('share/icons/hicolor/48x48/hildon', ['icons/48x48/sojourner.png']),
        # Yes, other apps put 64x64 icons in 'scalable'.
        ('share/icons/hicolor/scalable/hildon', ['icons/64x64/sojourner.png']),
        ('share/applications/hildon', ['sojourner.desktop']),
        ('share/sojourner/', ['sojourner.cfg']),
        # Data for the supported conferences        
        # TODO: Separate the conference data to its own package
        ('share/sojourner/conferences/fosdem2011', ['conferences/fosdem2011/banner.png']),
        ('share/sojourner/conferences/fosdem2011', ['conferences/fosdem2011/fosdem2011.cfg']),
        ('share/sojourner/conferences/meegofi2011', ['conferences/meegofi2011/banner.png']),
        ('share/sojourner/conferences/meegofi2011', ['conferences/meegofi2011/meegofi2011.cfg']),
        ('share/sojourner/conferences/rmll2011', ['conferences/rmll2011/banner.png']),
        ('share/sojourner/conferences/rmll2011', ['conferences/rmll2011/rmll2011.cfg']),
        ('share/sojourner/conferences/desktopsummit2011', ['conferences/desktopsummit2011/banner.png']),
        ('share/sojourner/conferences/desktopsummit2011', ['conferences/desktopsummit2011/desktopsummit2011.cfg']),
        ('share/sojourner/conferences/fosdem2012', ['conferences/fosdem2012/banner.png']),
        ('share/sojourner/conferences/fosdem2012', ['conferences/fosdem2012/fosdem2012.cfg']),
        ('share/sojourner/conferences/fosdem2014', ['conferences/fosdem2014/banner.png']),
        ('share/sojourner/conferences/fosdem2014', ['conferences/fosdem2014/fosdem2014.cfg']),
        ('share/sojourner/conferences/fosdem2015', ['conferences/fosdem2015/banner.png']),
        ('share/sojourner/conferences/fosdem2015', ['conferences/fosdem2015/fosdem2015.cfg']),
        ('share/sojourner/conferences/fosdem2016', ['conferences/fosdem2016/banner.png']),
        ('share/sojourner/conferences/fosdem2016', ['conferences/fosdem2016/fosdem2016.cfg']),
        ('share/sojourner/conferences/fosdem2017', ['conferences/fosdem2017/banner.png']),
        ('share/sojourner/conferences/fosdem2017', ['conferences/fosdem2017/fosdem2017.cfg']),
    ],
    license='GPL v3',
)

