from Tag import Tag


class Token(object):
    def __init__(self, tag, attribute=None):
        self.tag = tag
        self.attribute = attribute

    def copy(self):
        return Token(self.tag, self.attribute)

    def __str__(self):
        if self.tag == Tag.ID or self.tag == Tag.NUM:
            return self.attribute
        else:
            return Tag.get_token_tag_name(self)
