/*
	Nick Caravaggio

	December 6, 2020

	CS A250 (C++ 2)
	Project 2: With a list of kingdoms, from a text file, organize and append into containers, and sort it in meaningful ways through an easy-to-use CLI-application.
*/

#ifndef CANDIDATETYPE_H
#define CANDIDATETYPE_H

#include "CharacterType.h"

const int NUM_OF_KINGDOMS = 7;	// constant global for capacity of array.
const std::string KINGDOMS[] = {
	"The North",
	"The Vale",
	"The Stormlands",
	"The Reach",
	"The Westerlands",
	"The Iron Islands",
	"Dorne"
};

class CandidateType : public CharacterType
{
public:
	// Default constructor
	CandidateType();
	// Copy constructor
	CandidateType(const CandidateType& otherCandidateType);

	// Copy assignment operator
	CandidateType& operator=(const CandidateType& otherCandidateType);
	// Comparison Operator
	bool operator==(int) const;

	// updateVotesByKingdom
	void updateVotesByKingdom(int index, int numOfVotes);

	// getTotalVotes
	int getTotalVotes() const;
	// getVotesByKingdom
	int getVotesByKingdom(int index) const;

	// printCandidateInfo
	void printCandidateInfo() const;
	// printCandidateTotalVotes
	void printCandidateTotalVotes() const;

	// Destructor
	~CandidateType();

private:
	int totalVotes;
	int numOfKingdoms;
	int* kingdomVotes;
};

#endif