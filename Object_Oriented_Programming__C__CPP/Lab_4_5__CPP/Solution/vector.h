#ifndef OOP_A4_5_916_SABAILA_CALIN_VECTOR_H
#define OOP_A4_5_916_SABAILA_CALIN_VECTOR_H

template <typename T>
class vector
{
private:
    T **elem;
    int nrElem, cap;

    void Resize();

public:
    vector();
    ~vector();

    void push_back(const T &element);
    void pop_back();

    T &operator[](int idx);

    int size();
    int capacity();
};

// This function is the constructor of the vector class
// It initializes the number of elements to 0, the capacity to 1 and allocates memory for the elements
// @param: none
// @return: none
template <typename T>
vector <T>::vector()
{
    this -> nrElem = 0;
    this -> cap = 1;
    this -> elem = new T*[1];
}

// This function is the destructor of the vector class
// It deallocates memory for the elements
// @param: none
// @return: none
template <typename T>
vector <T>::~vector()
{
    for (int i = 0; i < this -> nrElem; i++)
    {
        delete this -> elem[i];
    }
    delete[] this -> elem;
}

// This function overloads the [] operator
// It returns the element at the given index
// @param idx: an integer representing the index of the element
// @throws: a string exception if the index is out of range
// @return: a reference to the element at the given index
template <typename T>
T &vector <T>::operator[](int idx)
{
    if (idx < 0 || idx >= this -> nrElem)
        throw std::string("Index " + std::to_string(idx) + " is out of range");

    return *this -> elem[idx];
}

// This function resizes the vector
// It doubles the capacity of the vector and copies the elements to the new vector
// @param: none
// @return: none
template <typename T>
void vector <T>::Resize()
{
    this -> cap *= 2;
    T **temp = new T*[this -> cap];

    for (int i = 0; i < this -> nrElem; i++)
    {
        temp[i] = this -> elem[i];
    }
    delete[] this -> elem;

    this -> elem = temp;
}

// This function adds an element to the vector
// It adds the element to the end of the vector
// @param element: a reference to the element that will be added
// @return: none
template <typename T>
void vector <T>::push_back(const T &element)
{
    if (this -> nrElem == this -> cap)
        this -> Resize();

    this -> elem[this -> nrElem] = new T(element);
    this -> nrElem++;
}

// This function removes an element from the vector
// It removes the last element from the vector
// @param: none
// @throws: a string exception if the vector is empty
// @return: none
template <typename T>
void vector <T>::pop_back()
{
    if (this -> nrElem <= 0)
        throw std::string("Cannot pop any more elements");

    delete this -> elem[this -> nrElem - 1];
    this -> nrElem--;
}

// This function returns the number of elements in the vector
// @param: none
// @return: an integer representing the number of elements in the vector
template <typename T>
int vector <T>::size()
{
    return this -> nrElem;
}

// This function returns the capacity of the vector
// @param: none
// @return: an integer representing the capacity of the vector
template <typename T>
int vector <T>::capacity()
{
    return this -> cap;
}

#endif //OOP_A4_5_916_SABAILA_CALIN_VECTOR_H
//