PLUGIN_NAME = 'Duplicate File Processor'
PLUGIN_AUTHOR = 'Phoenix Osiris'
PLUGIN_DESCRIPTION = 'Checks For Duplicate Files'
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.16"]

from picard.plugin import register_processor
from picard import log
from picard.ui.itemviews import ClusterItem
from picard.cluster import Cluster
from picard.track import Track

class RemoveItems(Cluster):
	def __init__(self):
		super(RemoveItems, self).__init__(_(u"Remove Items"), special=True)

	def add_files(self, files):
		Cluster.add_files(self, files)
		self.tagger.window.enable_cluster(self.get_num_files() > 0)

	def add_file(self, file):
		Cluster.add_file(self, file)
		self.tagger.window.enable_cluster(self.get_num_files() > 0)

	def remove_file(self, file):
		Cluster.remove_file(self, file)
		self.tagger.window.enable_cluster(self.get_num_files() > 0)

	def lookup_metadata(self):
		return False

	def can_edit_tags(self):
		return False

	def can_autotag(self):
		False

	def can_view_info(self):
		return False
		
_removeItem = RemoveItems()

def on_file_move(file, other):
	log.debug("TF Move File ")
	log.debug(file)
	log.debug(other)
	
	log.debug(file.parent[0])
	
	if not isinstance(file[0], Track):
		return


	for otherFile in file.parent[0]:
		log.debug("here")
		#log.debug("MoveFileCompare: " + file[0].metadata.compare(otherFile))
		# file.move(_removeItem)		
	
def on_treeview_init(treeview, other):
	log.debug("TF Tree View")
	treeview[0].unmatched_files2 = ClusterItem(_removeItem, False, treeview[0])
	treeview[0].unmatched_files2.update()

	
register_processor("file_plugin_processor_move", on_file_move)
register_processor("FileTreeView-Init", on_treeview_init)
