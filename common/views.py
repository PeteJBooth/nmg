# django core
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.detail import BaseDetailView

# local
from filer.models import Image

# ----------------------------------------------------------------------------

class FilerImage(BaseDetailView):
	model = Image

	def get(self, request, *args, **kwargs):
		#import pdb;pdb.set_trace();
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		#import pdb;pdb.set_trace();
		return self.render_to_response(context)

class FilerImageList(ListView):
    model = Image

    def get_context_data(self, **kwargs):
		context = super(FilerImageList,self).get_context_data(**kwargs)
		image_dict = []
		for image in context['image_list']:
			image_dict.append("{{title:'{0}/{1}',value:'{2}'}}".format(
				#image.logical_folder.quoted_logical_path,image.label,reverse('filer-image',kwargs={'pk':image.pk}))
				image.logical_folder.quoted_logical_path,image.label,image.url)
			)
		context['jsarray'] = ",".join(image_dict)
		return context

