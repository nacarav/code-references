/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#include "CharacterType.h"

using namespace std;

// overloaded constructor
CharacterType::CharacterType(const string& fName, const string& lName, int idx)
{
	firstName = fName;
	lastName = lName;
	id = idx;
}

// Set character info function
void CharacterType::setCharacterInfo(const std::string& fName, const std::string& lName, int idx)
{
	firstName = fName;
	lastName = lName;
	id = idx;
}

// returns first name
std::string CharacterType::getFirstName() const
{
	return firstName;
}

// returns last name
std::string CharacterType::getLastName() const
{
	return lastName;
}

// returns ID
int CharacterType::getID() const
{
	return id;
}

// Prints id, first name and last name.
void CharacterType::printCharacterInfo() const
{
	printID();
	cout << " " << firstName << " " << lastName;
}

// prints last name and first name.
void CharacterType::printName() const
{
	cout << lastName << ", " << firstName;
}

// prints ID only.
void CharacterType::printID() const
{
	cout << " ID# " << getID();
}

// Destructor
CharacterType::~CharacterType()
{
}