/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#include "CandidateType.h"

using namespace std;

// Default constructor
CandidateType::CandidateType()
{
	totalVotes = 0;
	numOfKingdoms = NUM_OF_KINGDOMS;
	kingdomVotes = new int[numOfKingdoms] {0};
}

// copy constructor
CandidateType::CandidateType(const CandidateType& otherCandidateType)
	: CharacterType(otherCandidateType.getFirstName(), otherCandidateType.getLastName(), otherCandidateType.getID())
{
	totalVotes = otherCandidateType.totalVotes;
	numOfKingdoms = otherCandidateType.numOfKingdoms;
	kingdomVotes = new int[numOfKingdoms];

	for (int i = 0; i < numOfKingdoms; i++)
		kingdomVotes[i] = otherCandidateType.kingdomVotes[i];
}

// copy assignment operator
CandidateType& CandidateType::operator=(const CandidateType& otherCandidateType)
{
	if (&otherCandidateType != this)
	{
		setCharacterInfo(otherCandidateType.getFirstName(), otherCandidateType.getLastName(), otherCandidateType.getID());
		totalVotes = otherCandidateType.totalVotes;
		numOfKingdoms = otherCandidateType.numOfKingdoms;

		for (int i = 0; i < numOfKingdoms; i++)
		{
			kingdomVotes[i] = otherCandidateType.kingdomVotes[i];
		}
	}
	else
	{
		cerr << "Attempted assignment to itself.";
	}
	return *this;
}

bool CandidateType::operator==(int idNumber) const
{
	return getID() == idNumber;
}

// updates total votes and kingdom votes
void CandidateType::updateVotesByKingdom(int idx, int newVotes)
{
	kingdomVotes[idx] =  newVotes;
	totalVotes += newVotes;
}

// returns the total votes of candidate
int CandidateType::getTotalVotes() const
{
	return totalVotes;
}

// getVotesByKingdom
int CandidateType::getVotesByKingdom(int idx) const
{
	return kingdomVotes[idx];
}

// prints candidate's id, last name and first name
void CandidateType::printCandidateInfo() const
{
	printID();
	cout << " - ";
	printName();
}

// prints candidate's name and total votes.
void CandidateType::printCandidateTotalVotes() const
{
	printName();
	cout << "\n	Total Votes(all kingdoms): " << totalVotes;
}

// destructor
CandidateType::~CandidateType()
{
	delete[] kingdomVotes;
	kingdomVotes = NULL;
}