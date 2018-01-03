from . import MD5Folder

class AfpFolder(MD5Folder):

    def tree_complete(self):
        MD5Folder.tree_complete(self)

        # findall needs xpath or it'll only search direct children
        names = []
        geo_names = []
        for tag in self.info_kbin.xml_doc.findall('.//' + self.md5_tag):
            name = tag.attrib['name']
            names.append(name)
            for geo in tag.findall('geo'):
                for shape in self._split_ints(geo.text):
                    geo_names.append('{}_shape{}'.format(name, shape))

        self._apply_md5_folder(names, self.folders['bsi'])
        self._apply_md5_folder(geo_names, self.parent.folders['geo'])
