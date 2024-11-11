#include <stdio.h>
#include <stdlib.h>

// Define a structure for a tree node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Define a structure for a stack node
struct StackNode {
    struct Node* treeNode;
    struct StackNode* next;
};

// Function to create a new tree node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to create a new stack node
struct StackNode* createStackNode(struct Node* treeNode) {
    struct StackNode* newStackNode = (struct StackNode*)malloc(sizeof(struct StackNode));
    newStackNode->treeNode = treeNode;
    newStackNode->next = NULL;
    return newStackNode;
}

// Function to push a node onto the stack
void push(struct StackNode** top, struct Node* treeNode) {
    struct StackNode* newStackNode = createStackNode(treeNode);
    newStackNode->next = *top;
    *top = newStackNode;
}

// Function to pop a node from the stack
struct Node* pop(struct StackNode** top) {
    if (*top == NULL) {
        return NULL; // Stack is empty
    }
    struct StackNode* temp = *top;
    struct Node* poppedNode = temp->treeNode;
    *top = (*top)->next;
    free(temp);
    return poppedNode;
}

// Function to check if stack is empty
int isEmpty(struct StackNode* top) {
    return top == NULL;
}

// Function to insert a new value into the binary tree
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else {
        root->right = insert(root->right, data);
    }
    return root;
}

// Iterative function to search for a value in the binary tree using a stack
int searchIterative(struct Node* root, int data) {
    struct StackNode* stack = NULL; // Initialize stack
    struct Node* currentNode = root;

    while (currentNode != NULL || !isEmpty(stack)) {
        // Traverse to the leftmost node
        while (currentNode != NULL) {
            push(&stack, currentNode); // Push current node onto stack
            currentNode = currentNode->left;
        }

        // Pop the top node from the stack
        currentNode = pop(&stack);
        if (currentNode == NULL) {
            break; // Safety check
        }

        // Check if the popped node is the target
        if (currentNode->data == data) {
            return 1; // Value found
        }

        // Move to the right node
        currentNode = currentNode->right;
    }

    return 0; // Value not found
}

// Function to print the tree in-order (for verification)
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// Main function to demonstrate insertion and search
int main() {
    struct Node* root = NULL;
    
    // Insert values into the binary tree
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    
    // Print in-order traversal of the tree
    printf("In-order traversal: ");
    inorder(root);
    printf("\n");

    // Search for values using stack-based search
    int searchValue = 40;
    if (searchIterative(root, searchValue)) {
        printf("%d found in the tree.\n", searchValue);
    } else {
        printf("%d not found in the tree.\n", searchValue);
    }

    searchValue = 90;
    if (searchIterative(root, searchValue)) {
        printf("%d found in the tree.\n", searchValue);
    } else {
        printf("%d not found in the tree.\n", searchValue);
    }

    return 0;
}
