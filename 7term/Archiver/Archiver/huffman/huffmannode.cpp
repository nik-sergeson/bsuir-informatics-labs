#include "huffmannode.h"

HuffmanNode::HuffmanNode(int ch)
{
    count_=0;
    value_=ch;
    depth_=0;
    parent_=NULL;
    left_=NULL;
    right_=NULL;
}

HuffmanNode::HuffmanNode(int ch, int count){
    count_=count;
    value_=ch;
    depth_=0;
    parent_=NULL;
    left_=NULL;
    right_=NULL;
}

int HuffmanNode::count() const{
    return count_;
}

int HuffmanNode::value() const{
    return value_;
}

int HuffmanNode::depth() const{
    return depth_;
}

HuffmanNode* HuffmanNode::left() const{
    return left_;
}

HuffmanNode* HuffmanNode::right() const{
    return right_;
}

HuffmanNode* HuffmanNode::parent() const{
    return parent_;
}

int HuffmanNode::CompareNodes(const void *first, const void *second){
    return (*(HuffmanNode **)first)->count()-(*(HuffmanNode **)second)->count();
}

void HuffmanNode::setparent(HuffmanNode *parent){
    parent_=parent;
}

void HuffmanNode::setdepth(int depth){
    depth_=depth;
}

HuffmanNode::HuffmanNode(HuffmanNode *left, HuffmanNode *right){
    left_=left;
    right_=right;
    count_=left->count()+right->count();
    parent_=NULL;
    depth_=0;
    value_=COMBINE_NODE;
    left->setparent(this);
    right->setparent(this);
}

HuffmanNode::~HuffmanNode(){
    if(left_!=NULL)
        delete left_;
    if(right_!=NULL)
        delete right_;

}

void HuffmanNode::IncreaseCount(int count){
    count_+=count;
}

void HuffmanNode::DecreaseCount(int count){
    count_-=count;
}

HuffmanNode::HuffmanNode(const HuffmanNode* h_node){
    value_=h_node->value();
    count_=h_node->count();
    depth_=h_node->depth();
    parent_=NULL;
    left_=NULL;
    right_=NULL;
}
