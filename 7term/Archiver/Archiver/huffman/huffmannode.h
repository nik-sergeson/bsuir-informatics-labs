#ifndef HUFFMANNODE_H
#define HUFFMANNODE_H
#include <cstdlib>

#define COMBINE_NODE -1

class HuffmanNode
{
public:
    HuffmanNode(int ch);
    HuffmanNode(int ch, int count);
    HuffmanNode(const HuffmanNode* h_node);
    HuffmanNode(HuffmanNode *left, HuffmanNode *right);
    int value() const;
    int count() const;
    int depth() const;
    HuffmanNode* left() const;
    HuffmanNode* right() const;
    HuffmanNode* parent() const;
    void setparent(HuffmanNode *parent);
    void setdepth(int depth);
    void IncreaseCount(int count);
    void DecreaseCount(int count);
    static int CompareNodes(const void * first, const void * second);
    ~HuffmanNode();
private:
    int value_;
    int count_;
    int depth_;
    HuffmanNode *left_, *right_, *parent_;
};

#endif // HUFFMANNODE_H
