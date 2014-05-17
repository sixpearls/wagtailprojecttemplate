{{ project_name|title }} with Wagtail
=====================================

You should write some docs, it's good for the soul.

[Wagtail](http://wagtail.io) is distributed as a Python package, to be incorporated into a Django project via the INSTALLED_APPS setting. To get you up and running quickly, we provide a demo site with all the configuration in place, including a set of example page types.


Setup (with Vagrant)
-----------------------

We recommend running {{ project_name }} on wagtail in a virtual machine using Vagrant, as this ensures that the correct dependencies are in place regardless of how your host machine is set up.

### Dependencies

* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant 1.1+](http://www.vagrantup.com)

### Installation

Run the following commands:

    django-admin.py startproject --template=https://github.com/sixpearls/wagtailprojecttemplate/zipball/master -evf,py,rst,md <project_name>
    cd {{ project_name }}
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    fab manage:createsuperuser
    fab serve

This will make the app accessible on the host machine as http://localhost:8111/ - you can access the Wagtail admin interface at http://localhost:8111/admin/ . Begin adding pages at http://localhost:8111/admin/pages/ The codebase is located on the host machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

### Developing Wagtail

The above setup is all you need for trying out the demo site and building Wagtail-powered sites. To develop Wagtail itself, you'll need a working copy of [the Wagtail codebase](https://github.com/torchbox/wagtail) alongside your demo site, shared with your VM so that it is picked up instead of the packaged copy of Wagtail. From the location where you cloned wagtaildemo:

    git clone https://github.com/torchbox/wagtail.git
    cd wagtaildemo
    cp Vagrantfile.local.example Vagrantfile.local
        (edit Vagrantfile.local to specify the path to the wagtail codebase, if required)
        (edit the rest of local.py as appropriate, especially uncomment the lines from 'import sys' onward )
    
If your VM is currently running, you'll then need to run `vagrant halt` followed by `vagrant up` for the changes to take effect.

Usage
-----

Use the ``fab`` helper(s). Just make sure to update (and deploy) the ``local.py`` file::

    $ fab serve # launch development server from vagrant
    $ fab collectstatic # collect static files

