package main;

public class LinkedListADT {

	
	public static void main(String[] args) {
		System.out.println("Hello Linked List ADT");

	}

}


public class Node {
    public int data;
    public Node next;
    public Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class LinkedList {
    private Node head;
    private Node tail;
    private int size;

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    public boolean isEmpty() {
        return this.head == null;
    }

    public void insertHead(int data) {
        Node new_node = new Node(data);
        if (isEmpty()) {
            this.tail = new_node;
        } else {
            this.head.prev = new_node;
        }
        new_node.next = this.head;
        this.head = new_node;
        this.size++;
    }

    public int removeHead() {
        if (isEmpty()) {
            return -1;
        }
        Node removed_node = this.head;
        this.head = removed_node.next;
        if (this.head == null) {
            this.tail = null;
        } else {
            this.head.prev = null;
        }
        this.size--;
        return removed_node.data;
    }

    public void insertTail(int data) {
        Node new_node = new Node(data);
        if (isEmpty()) {
            this.head = new_node;
        } else {
            this.tail.next = new_node;
            new_node.prev = this.tail;
        }
        this.tail = new_node;
        this.size++;
    }

    public int removeTail() {
        if (isEmpty()) {
            return -1;
        }
        Node removed_node = this.tail;
        this.tail = removed_node.prev;
        if (this.tail == null) {
            this.head = null;
        } else {
            this.tail.next = null;
        }
        this.size--;
        return removed_node.data;
    }

    public void insertAtPos(int data, int pos) {
        if (pos < 0 || pos > this.size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        if (pos == 0) {
            insertHead(data);
            return;
        }
        if (pos == this.size) {
            insertTail(data);
            return;
        }
        Node new_node = new Node(data);
        Node curr_node = this.head;
        for (int i = 0; i < pos-1; i++) {
            curr_node = curr_node.next;
        }
        new_node.next = curr_node.next;
        new_node.prev = curr_node;
        curr_node.next.prev = new_node;
        curr_node.next = new_node;
        this.size++;
    }

    public void traverse() {
        Node curr_node = this.head;
        while (curr_node != null) {
            System.out.print(curr_node.data + " ");
            curr_node = curr_node.next;
        }
        System.out.println();
    }
}
