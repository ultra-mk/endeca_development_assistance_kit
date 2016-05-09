from setuptools import setup

setup(name='edak',
	entry_points={
		'console_scripts' :[
			'edak = edak.__main__:main']
	}
	)