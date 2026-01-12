package main


func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	shortest := strs[0]
	for _, s := range strs {
		if len(s) < len(shortest) {
			shortest = s
		}
	}

	for i := 0; i < len(shortest); i++ {
		for _, s := range strs {
			if s[i] != shortest[i] {
				return shortest[:i]
			}
		}
	}
	return shortest

}