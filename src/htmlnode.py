class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        if not self.props:
            return ""

        html = ""

        for key, value in self.props.items():
            html  += f' {key}="{value}"'

        return html
    def __repr__(self):
        return (
            f"HTMLNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props})"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (
            f"LeafNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props})"
        )

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)


    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")

        if not self.children:
            raise ValueError("ParentNode must have children")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()


        return (
            f"<{self.tag}{self.props_to_html()}>"
            f"{children_html}"
            f"</{self.tag}>"
        )
